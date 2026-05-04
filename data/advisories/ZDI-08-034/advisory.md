# ZDI-08-034: Hewlett-Packard StorageWorks Storage Mirroring Authentication Processing Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-034
- **ZDI-CAN:** ZDI-CAN-185
- **Date:** 2008-06-04
- **CVE:** CVE-2008-1661
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** StorageWorks
- **Credit:** Titon of BastardLabs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-034/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett Packard StorageWorks Storage Mirroring. Authentication is not required to exploit this vulnerability. The specific flaw exists in the DoubleTake.exe process bound by default on TCP ports 1100, 1106 and UDP port 1105. During the handling of an encoded authentication request, the process copies the user-supplied login information into a fixed length stack buffer. Sending at least 256 bytes will trigger a stack based buffer overflow due to a vulnerable processing loop. Exploitation of this issue can result in arbitrary code execution.

## Additional Details

To resolve this vulnerability download HP StorageWorks Storage Mirroring software v4.5 Service Pack 2 (SP2) from Double-Take at the following URL: http://www.doubletake.com/products/double-take/default.aspx

## Disclosure Timeline

- 2007-05-22 - Vulnerability reported to vendor
- 2008-06-04 - Coordinated public release of advisory
