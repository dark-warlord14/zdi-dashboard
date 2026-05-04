# ZDI-15-465: Adobe Reader Arbitrary File Deletion Sandbox Escape Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-465
- **ZDI-CAN:** ZDI-CAN-2892
- **Date:** 2015-10-13
- **CVE:** CVE-2015-7829
- **CVSS:** 1.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:N/I:N/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** AbdulAziz Hariri and Jasiel Spelman of HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-465/
## Vulnerability Details

This vulnerability allows local attackers to delete arbitrary files on vulnerable installations of Adobe Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of junction points. An attacker running code in the context of a sandboxed Adobe Reader process can set up a junction point in the Synchronizer folder and then run Adobe Collaboration Sync which will delete the contents of the folder. An attacker can leverage this vulnerability to delete files as a normal user from a sandboxed process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb15-24.html

## Disclosure Timeline

- 2015-04-28 - Vulnerability reported to vendor
- 2015-10-13 - Coordinated public release of advisory
