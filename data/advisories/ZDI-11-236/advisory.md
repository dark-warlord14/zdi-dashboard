# ZDI-11-236: EMC Documentum eRoom Indexing Server OpenText HummingBird Connector Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-236
- **ZDI-CAN:** ZDI-CAN-1079
- **Date:** 2011-07-18
- **CVE:** CVE-2011-1741
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** EMC
- **Affected Products:** Documentum eRoom
- **Credit:** Stephen Fewer of Harmony Security (www.harmonysecurity.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-236/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of EMC Documentum eRoom Indexing Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the bundled implementation of OpenText's HummingBird Connector. When parsing a particular packet received from a TCP connection, the application will attempt to copy part of the packet's contents into a buffer located on the stack. Due to not completely accommodating for the size of the data in the packet, the application will overwrite variables positioned after the buffer. This can lead to code execution under the context of the server.

## Additional Details

EMC has issued an update to correct this vulnerability. More details can be found at: http://www.securityfocus.com/archive/1/518897/30/0/threaded

## Disclosure Timeline

- 2011-01-21 - Vulnerability reported to vendor
- 2011-07-18 - Coordinated public release of advisory
