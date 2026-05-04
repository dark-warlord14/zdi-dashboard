# ZDI-11-291: Cisco Unified Service Monitor brstart add_dm Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-291
- **ZDI-CAN:** ZDI-CAN-1109
- **Date:** 2011-10-18
- **CVE:** CVE-2011-2738
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** EMC, Cisco
- **Affected Products:** ApplicationXtender Workflow
- **Credit:** AbdulAziz Hariri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-291/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Cisco Unified Service Monitor due to bundled EMC SMARTS application server. Authentication is not required to exploit this vulnerability. The flaw exists within the brstart.exe service which listens by default on TCP port 9002. When handling an add_dm request the process uses a user provided value to allocate a buffer then blindly copies user supplied data into a fixed-length buffer on the heap. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the casuser user.

## Additional Details

EMC has issued an update to correct this vulnerability. More details can be found at: http://www.securityfocus.com/archive/1/519646/30/0/threaded Cisco has issued an update to correct this vulnerability. More details can be found at: http://www.cisco.com/warp/public/707/cisco-sa-20110914-lms.shtml

## Disclosure Timeline

- 2011-02-17 - Vulnerability reported to vendor
- 2011-10-18 - Coordinated public release of advisory
