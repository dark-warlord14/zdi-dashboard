# ZDI-20-688: IBM WebSphere UploadFileArgument Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-688
- **ZDI-CAN:** ZDI-CAN-10732
- **Date:** 2020-06-05
- **CVE:** CVE-2020-4448
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** IBM
- **Affected Products:** WebSphere
- **Credit:** b0yd
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-688/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of IBM WebSphere. Authentication is not required to exploit this vulnerability. The specific flaw exists within the BroadcastMessageManager class. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: https://www.ibm.com/support/pages/node/6220336

## Disclosure Timeline

- 2020-04-17 - Vulnerability reported to vendor
- 2020-06-05 - Coordinated public release of advisory
- 2020-09-21 - Advisory Updated
