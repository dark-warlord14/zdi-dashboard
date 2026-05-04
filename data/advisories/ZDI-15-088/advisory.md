# ZDI-15-088: Microsoft Word Format Tag Transposition Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-088
- **ZDI-CAN:** ZDI-CAN-2530
- **Date:** 2015-03-12
- **CVE:** CVE-2015-0085
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Word
- **Credit:** 3S Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-088/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Word. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of the item1.xml file inside of the .docx package. By transposing elements, an attacker is able to cause a pointer to be re-used after it was freed. An attacker could leverage this to execute arbitrary code in the context of the user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-022

## Disclosure Timeline

- 2014-09-11 - Vulnerability reported to vendor
- 2015-03-12 - Coordinated public release of advisory
