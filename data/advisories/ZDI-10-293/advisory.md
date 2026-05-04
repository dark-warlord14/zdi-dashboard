# ZDI-10-293: HP StorageWorks Storage Mirroring DoubleTake.exe Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-293
- **ZDI-CAN:** ZDI-CAN-958
- **Date:** 2010-12-23
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** StorageWorks
- **Credit:** AbdulAziz Hariri of ThirdEyeTesters
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-293/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP StorageWorks Storage Mirroring. Authentication is not required to exploit this vulnerability. The flaw exists within the DoubleTake.exe component which listens by default on TCP port 6320. When handling an incoming packet the process blindly trusts a user supplied length for a copy of arbitrary data into a fixed-length buffer on the heap. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c02660122

## Disclosure Timeline

- 2010-09-27 - Vulnerability reported to vendor
- 2010-12-23 - Coordinated public release of advisory
