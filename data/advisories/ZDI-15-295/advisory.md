# ZDI-15-295: (Pwn2Own) Microsoft Internet Explorer ActiveX Install Broker Sandbox Escape Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-295
- **ZDI-CAN:** ZDI-CAN-2829
- **Date:** 2015-07-09
- **CVE:** CVE-2015-1743
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Yuki Chen of Qihoo 360
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-295/
## Vulnerability Details

This vulnerability allows attackers to escape the Enhanced Protection Mode sandbox of vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the use of the ActiveX install broker. The broker allows files to be installed to arbitrary paths from within the Internet Explorer sandbox and subsequently executed. An attacker can leverage this vulnerability to execute code under the context of the user at medium integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-056

## Disclosure Timeline

- 2015-02-16 - Vulnerability reported to vendor
- 2015-07-09 - Coordinated public release of advisory
