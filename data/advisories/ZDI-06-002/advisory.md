# ZDI-06-002: Adobe Macromedia ShockWave Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-002
- **ZDI-CAN:** ZDI-CAN-007
- **Date:** 2006-02-23
- **CVE:** CVE-2005-3525
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Adobe
- **Affected Products:** Flash Player
- **Credit:** Peter Vreugdenhil
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-002/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Macromedia Shockwave. Exploitation requires the target to visit a malicious web site. This specific flaw exists within the ActiveX control with CLSID 166B1BCA-3F9C-11CF-8075-444553540000. Specifying large values for two specific parameters to this control results in an exploitable stack based buffer overflow. Due to the nature of this vulnerability, the target user is not required to have fully completed an installation of Shockwave to be vulnerable.

## Additional Details

Adobe has fixed the issue in the Shockwave Player ActiveX installer. Since the vulnerability occurs in the installer, no action needs to be taken by current Macromedia Shockwave Player by Adobe customers. Customers downloading and installing the latest Shockwave Player are no longer vulnerable with the updated Shockwave Player ActiveX installer. The official vendor advisory is available at http://www.macromedia.com/devnet/security/security_zone/apsb06-02.html

## Disclosure Timeline

- 2005-11-22 - Vulnerability reported to vendor
- 2006-02-23 - Coordinated public release of advisory
