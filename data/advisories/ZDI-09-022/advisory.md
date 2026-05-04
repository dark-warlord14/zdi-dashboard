# ZDI-09-022: Apple Safari Malformed SVGList Parsing Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-022
- **ZDI-CAN:** ZDI-CAN-464
- **Date:** 2009-05-13
- **CVE:** CVE-2009-0945
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Nils
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-022/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists during the parsing of malformed SVGLists via the SVGPathList data structure, the following lists are affected: SVGTransformList, SVGStringList, SVGNumberList, SVGPathSegList, SVGPointList, SVGLengthList. When a negative index argument is suppled to the insertItemBefore() method, a memory corruption occurs resulting in the ability to execute arbitrary code.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT3549

## Disclosure Timeline

- 2009-03-19 - Vulnerability reported to vendor
- 2009-05-13 - Coordinated public release of advisory
