# ZDI-12-027: IBM SPSS VsVIEW6.ocx ActiveX Control SaveDoc Method Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-027
- **ZDI-CAN:** ZDI-CAN-1307
- **Date:** 2012-02-08
- **CVE:** CVE-2012-0189
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** IBM
- **Affected Products:** SPSS
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-027/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM SPSS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the SaveDoc function exposed by the VsVIEW6.ocx ActiveX control. The SaveDoc function causes a file to be created at an arbitrary path specified by the first argument (FileName). The file contents can be controlled by first setting the 'Text' member of the object. These behaviors can be exploited by a remote attacker to execute arbitrary code on the target system.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://www-01.ibm.com/support/docview.wss?uid=swg21577951

## Disclosure Timeline

- 2011-07-20 - Vulnerability reported to vendor
- 2012-02-08 - Coordinated public release of advisory
