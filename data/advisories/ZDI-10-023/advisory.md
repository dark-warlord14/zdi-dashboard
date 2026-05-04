# ZDI-10-023: Multiple Vendor librpc.dll Signedness Error Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-023
- **ZDI-CAN:** ZDI-CAN-298
- **Date:** 2010-03-01
- **CVE:** CVE-2009-2754
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** IBM, EMC
- **Affected Products:** Informix
- **Credit:** Sebastian Apelt (sebastian.apelt@siberas.de)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-023/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of both IBM Informix Dynamic Server and EMC Legato Networker. User interaction is not required to exploit this vulnerability. The specific flaw exists within the RPC protocol parsing library, librpc.dll, utilized by the ISM Portmapper service (portmap.exe) bound by default to TCP port 36890. During authentication, a lack of a proper signedness check on a supplied parameter size can result in exploitable stack based buffer overflow leading to arbitrary code execution under the context of the SYSTEM user.

## Additional Details

IBM states that this issue was first fixed in: IDS 10.00.TC9, IDS 11.10.TC3 Recommended fix pack version: IDS 10.00.TC10, IDS 11.10.TC3 4. URL to APAR or fixpack Fix pack download URL: http://www-933.ibm.com/support/fixcentral/ APAR URLs http://www.ibm.com/support/docview.wss?uid=swg1IC55329 http://www.ibm.com/support/docview.wss?uid=swg1IC55330 EMC has released a Security Advisory (ESA-08-007) identifier to customers through Powerlink.

## Disclosure Timeline

- 2008-02-07 - Vulnerability reported to vendor
- 2010-03-01 - Coordinated public release of advisory
