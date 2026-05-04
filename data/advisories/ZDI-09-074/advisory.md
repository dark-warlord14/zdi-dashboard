# ZDI-09-074: Multiple Vendor Hummingbird STR Service Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-074
- **ZDI-CAN:** ZDI-CAN-369
- **Date:** 2009-10-28
- **CVE:** N/A
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** EMC, OpenText, OpenText
- **Affected Products:** Documentum eRoom, Hummingbird, Search Server
- **Credit:** Stephen Fewer of Harmony Security (www.harmonysecurity.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-074/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on systems with vulnerable installations of EMC Documentum eRoom, OpenText Hummingbird and OpenText Search Server. Authentication is not required to exploit this vulnerability. The specific flaw exists in the Hummingbird STR service (STRsvc.exe) which listens by default on TCP port 10500. The STRlib.dll module receives network packet data into a static stack buffer. By providing a large enough packet, this buffer can overflow. Exploitation allows remote attackers to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

This issue has been resolved in EMC Documentum eRoom 7.4.2. EMC strongly recommends customers upgrade to EMC Documentum eRoom 7.4.2. More information on this can be found an powerlink.emc.com (Knowledge Base esg99041). This issue has been resolved in the latest Search Server 6.0 and 6.1 patches for all platforms. More information on the fix can be found in OpenText Knowledge Base 14816981 (login is required to access the content).

## Disclosure Timeline

- 2008-07-14 - Vulnerability reported to vendor
- 2009-10-28 - Coordinated public release of advisory
