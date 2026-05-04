# ZDI-08-022: Apple Safari WebKit PCRE Handling Integer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-022
- **ZDI-CAN:** ZDI-CAN-303
- **Date:** 2008-04-16
- **CVE:** CVE-2008-1026
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Charlie Miller, Jake Honoroff and Mark Daniel
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-022/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists in the regular expression compiler (JavaScriptCore/pcre/pcre_compile.cpp) in WebKit. When nesting regular expressions with large repetitions, a heap overflow occurs resulting in a condition allowing the execution of arbitrary code.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT1467

## Disclosure Timeline

- 2008-03-27 - Vulnerability reported to vendor
- 2008-04-16 - Coordinated public release of advisory
