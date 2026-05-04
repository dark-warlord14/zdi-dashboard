# ZDI-10-245: Microsoft Office PowerPoint Unknown Animation Node Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-245
- **ZDI-CAN:** ZDI-CAN-748
- **Date:** 2010-11-09
- **CVE:** CVE-2010-2573
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Office PowerPoint
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-245/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office Powerpoint 2003. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the application trusting a value defined within a file. This value will have some arithmetic performed on it, and subsequently be used as a counter for a processing loop. By modifying this value, an attacker can reliably corrupt memory. Successful exploitation will lead to code execution under the context of the application.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/ms10-088.mspx

## Disclosure Timeline

- 2010-06-02 - Vulnerability reported to vendor
- 2010-11-09 - Coordinated public release of advisory
