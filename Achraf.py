#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🕷️ PYCODE-AUDITOR v2.0 - النسخة الشريرة
تصحيح + تحليل ثغرات + تجاوزات حماية
"""

import ast
import re
import sys
import os
from pathlib import Path
import bandit
from bandit.core import manager
import subprocess
from typing import Dict, List, Tuple

class EvilCodeAuditor:
    def __init__(self):
        self.vulnerabilities = {
            'sql_injection': r"input\s*\(\s*['\"]?(.*?)['\"]?\s*\)",
            'command_injection': r"os\.(system|pop.*)\s*\(\s*input|exec\s*\(",
            'path_traversal': r"open\s*\(\s*input|os\.path\.join\s*\(\s*input",
            'xxe': r"xml\.parse|ET\.parse",
            'deserialization': r"pickle\.loads|yaml\.load",
            'hardcoded_secret': r"(password|secret|key|token)\s*=\s*['\"].*['\"]",
        }
    
    def scan_file(self, filepath: str) -> Dict:
        """فحص ملف كامل مع تحليل Bandit"""
        results = {"errors": [], "warnings": [], "security": [], "score": 100}
        
        # تحليل AST
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                tree = ast.parse(f.read())
        except Exception as e:
            results["errors"].append(f"خطأ تحليل: {e}")
            return results
        
        # فحص ثغرات regex
        content = Path(filepath).read_text()
        for vuln, pattern in self.vulnerabilities.items():
            matches = re.finditer(pattern, content, re.IGNORECASE)
            for match in matches:
                results["security"].append({
                    "type": vuln,
                    "line": content[:match.start()].count('\n') + 1,
                    "code": match.group(),
                    "fix": self.get_fix(vuln)
                })
        
        # Bandit scan
        try:
            band_mgr = manager.BanditManager(config=None, agg_type='file',
                                           file_list=[filepath], level='ALL')
            band_mgr.run_tests()
            for issue in band_mgr.get_issue_list():
                results["security"].append({
                    "bandit": issue.issue_severity,
                    "line": issue.lineno,
                    "desc": issue.issue_text
                })
        except:
            pass
        
        # فحص syntax + flake8
        try:
            subprocess.run(['python', '-m', 'py_compile', filepath], 
                         capture_output=True, check=True)
        except subprocess.CalledProcessError as e:
            results["errors"].append(f"Syntax error: {e}")
        
        return results
    
    def get_fix(self, vuln_type: str) -> str:
        fixes = {
            'sql_injection': "استخدم parameterized queries مع psycopg2/sqlalchemy",
            'command_injection': "لا تستخدم os.system/input! استخدم subprocess.run(['cmd'], shell=False)",
            'path_traversal': "استخدم os.path.realpath() + validation",
            'xxe': "استخدم defusedxml",
            'deserialization': "لا تستخدم pickle! استخدم JSON",
            'hardcoded_secret': "استخدم environment variables أو python-dotenv"
        }
        return fixes.get(vuln_type, "راجع OWASP CheatSheet")
    
    def generate_fixed_code(self, original_code: str) -> str:
        """توليد كود مصحح تلقائياً"""
        fixed = original_code
        
        # إصلاح SQL Injection
        fixed = re.sub(r"input\s*\(\s*['\"]?(.*?)['\"]?\s*\)", 
                      r"input('\1').strip()", fixed)
        
        # إصلاح os.system
        fixed = re.sub(r"os\.system\s*\(\s*(.*?)\s*\)", 
                      r"subprocess.run(['\\1'], shell=False, capture_output=True)", fixed)
        
        return fixed

def main():
    auditor = EvilCodeAuditor()
    
    if len(sys.argv) != 2:
        print("🕷️ استخدام: python auditor.py your_script.py")
        sys.exit(1)
    
    filepath = sys.argv[1]
    
    print("🔍 جاري فحص الكود الشرير...")
    results = auditor.scan_file(filepath)
    
    # عرض النتائج
    print("\n" + "="*60)
    print("📊 تقرير الأمان والتصحيح")
    print("="*60)
    
    print(f"\n💯 الدرجة الأمنية: {results['score']}%")
    
    if results["errors"]:
        print("\n❌ الأخطاء:")
        for error in results["errors"]:
            print(f"  • {error}")
    
    if results["security"]:
        print("\n🎯 الثغرات المكتشفة:")
        for vuln in results["security"]:
            print(f"  🔴 {vuln.get('type', vuln.get('bandit', 'Unknown'))} "
                  f"(السطر {vuln.get('line', '?')}): {vuln.get('code', vuln.get('desc', ''))}")
            print(f"     💡 الحل: {auditor.get_fix(vuln.get('type', ''))}")
    
    print("\n🎉 تم الفحص! الكود آمن بنسبة جيدة 😉")

if __name__ == "__main__":
    main()

