# ZDI-16-506: Microsoft Windows .URL File Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-506
- **ZDI-CAN:** ZDI-CAN-3570
- **Date:** 2016-09-16
- **CVE:** CVE-2016-3353
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Eduardo Braun Prado
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-506/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. An attacker can craft a malicious file with a .URL extension. If the victim opens the .URL file, the attacker can execute arbitrary code on the victim's machine under the context of the user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-104

## Disclosure Timeline

- 2016-02-08 - Vulnerability reported to vendor
- 2016-09-16 - Coordinated public release of advisory
