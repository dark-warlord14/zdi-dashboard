# ZDI-09-035: Microsoft Word Document Stack Based Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-035
- **ZDI-CAN:** ZDI-CAN-365
- **Date:** 2009-06-10
- **CVE:** CVE-2009-0563
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Word
- **Credit:** ling & wushi of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-035/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Word. User interaction is required to exploit this vulnerability in that the target must visit a malicious page, open a malicious e-mail, or open a malicious file. The specific flaw exists within the parsing of vulnerable tags inside a Microsoft Word document. Microsoft Word trusts a length field read from the file which is used to read file contents into a buffer allocated on the stack. When an invalid length is present, a stack based buffer overflow occurs, resulting in the ability to execute arbitrary code.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS09-027.mspx

## Disclosure Timeline

- 2008-07-08 - Vulnerability reported to vendor
- 2009-06-10 - Coordinated public release of advisory
