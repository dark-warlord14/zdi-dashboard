# ZDI-11-292: Cisco Unified Service Monitor brstart sm_read_string_length Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-292
- **ZDI-CAN:** ZDI-CAN-1258
- **Date:** 2011-10-18
- **CVE:** CVE-2011-2738
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Cisco, EMC
- **Affected Products:** ApplicationXtender Workflow
- **Credit:** AbdulAziz Hariri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-292/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Cisco Unified Service Monitor due to bundled EMC SMARTS application server. Authentication is not required to exploit this vulnerability. The flaw exists within the brstart.exe service which listens by default on TCP port 9002. When handling the authentication portion of a SMARTS request the process extracts a user provided value to allocate a buffer via sm_read_string_length then blindly copies user supplied data into this buffer on the heap. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the service.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: http://www.cisco.com/warp/public/707/cisco-sa-20110914-lms.shtml EMC has issued an update to correct this vulnerability. More details can be found at: http://www.securityfocus.com/archive/1/519646/30/0/threaded

## Disclosure Timeline

- 2011-06-07 - Vulnerability reported to vendor
- 2011-10-18 - Coordinated public release of advisory
