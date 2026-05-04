# ZDI-16-277: Microsoft Windows Media Center .MCL File Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-277
- **ZDI-CAN:** ZDI-CAN-3568
- **Date:** 2016-05-10
- **CVE:** CVE-2016-0185
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows Media Center
- **Credit:** Eduardo Braun Prado
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-277/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows Media Center. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. An attacker can craft a malicious file with a .MCL extension. Contained within the .MCL file is a URL that points to a second crafted file of type .LNK or .URL. If the victim opens the .MCL file, the attacker can execute arbitrary code on the victim's machine under the context of the user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms16-059.aspx

## Disclosure Timeline

- 2016-02-08 - Vulnerability reported to vendor
- 2016-05-10 - Coordinated public release of advisory
