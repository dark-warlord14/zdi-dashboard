# ZDI-06-014: Verisign I-Nav ActiveX Control Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-014
- **ZDI-CAN:** ZDI-CAN-030
- **Date:** 2006-05-10
- **CVE:** CVE-2006-2273
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Verisign
- **Affected Products:** I-Nav
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-014/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Verisign i-Nav ActiveX control. User interaction is required to exploit this vulnerability in that the target must visit a malicious web page. The specific flaw exists within the "VUpdater.Install" ActiveX control which is used to provide native support for Internationalized Domain Names (IDNs) in Microsoft Internet Explorer, Microsoft Outlook and Microsoft Outlook Express. Due to the lack of verification on Microsoft Cabinet (.CAB) files from the "InstallProduct" routine, an attacker can specify an arbitrary executable to run under the context of the current user.

## Additional Details

Verisign has issued an update to correct this vulnerability. More details can be found at: http://www.idnnow.com/

## Disclosure Timeline

- 2006-03-27 - Vulnerability reported to vendor
- 2006-05-10 - Coordinated public release of advisory
