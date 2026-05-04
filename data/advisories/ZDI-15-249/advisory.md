# ZDI-15-249: Microsoft Internet Explorer Add-On Installer EPM Sandbox Escape Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-249
- **ZDI-CAN:** ZDI-CAN-2796
- **Date:** 2015-06-11
- **CVE:** CVE-2015-1739
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Thomas Vanhoutte
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-249/
## Vulnerability Details

This vulnerability allows attackers to escape the Extended Protection Mode sandbox of vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the actions of the IE add-on installer. The installer can take a web page created by attacker code running in the context of the IE App Container and copy it to a location where it can be rendered as an Intranet webpage, which, by default, invokes IE as a medium-integrity process in the context of the user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-056

## Disclosure Timeline

- 2015-03-05 - Vulnerability reported to vendor
- 2015-06-11 - Coordinated public release of advisory
