# ZDI-19-773: Adobe Photoshop JSX File ExtendScript File.read Insufficient UI Warning Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-773
- **ZDI-CAN:** ZDI-CAN-8501
- **Date:** 2019-08-27
- **CVE:** CVE-2019-7989
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Photoshop
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-773/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Adobe Photoshop. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the File.read method when processing JSX files. When opening a JSX file, the user interface fails to warn the user of unsafe actions. An attacker can leverage this vulnerability to disclose information in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/photoshop/apsb19-44.html

## Disclosure Timeline

- 2019-05-09 - Vulnerability reported to vendor
- 2019-08-27 - Coordinated public release of advisory
