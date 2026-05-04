# ZDI-10-077: Adobe Download Manager Atlcom.get_atlcom ActiveX Control Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-077
- **ZDI-CAN:** ZDI-CAN-615
- **Date:** 2010-04-21
- **CVE:** CVE-2010-1278
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Adobe
- **Affected Products:** Download Manager
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-077/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Adobe Download Manager. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists within the gp.ocx ActiveX control. This control has a CLSID of {E2883E8F-472F-4fb0-9522-AC9BF37916A7} and the ProgID Atlcom.get_atlcom. Upon initialization this control copies the values from two parameters into a fixed length buffer. If supplied with large enough values this can lead lead to a buffer overflow that can be leveraged to execute arbitrary code under the context of the user running the browser.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb10-02.html

## Disclosure Timeline

- 2009-12-04 - Vulnerability reported to vendor
- 2010-04-21 - Coordinated public release of advisory
