# ZDI-19-771: Adobe Photoshop JSX File ExtendScript File.writeln Insufficient UI Warning Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-771
- **ZDI-CAN:** ZDI-CAN-8499
- **Date:** 2019-08-27
- **CVE:** CVE-2019-7989
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Photoshop
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-771/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe Photoshop. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the File.writeln method when processing JSX files. When opening a JSX file, the user interface fails to warn the user of unsafe actions. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/photoshop/apsb19-44.html

## Disclosure Timeline

- 2019-05-09 - Vulnerability reported to vendor
- 2019-08-27 - Coordinated public release of advisory
