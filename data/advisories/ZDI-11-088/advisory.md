# ZDI-11-088: Cisco Security Agent Management st_upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-088
- **ZDI-CAN:** ZDI-CAN-919
- **Date:** 2011-02-16
- **CVE:** CVE-2011-0364
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Cisco
- **Affected Products:** Security Agent Management Console
- **Credit:** Gerry Eisenhaur
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-088/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Cisco Security Agent Management Console. Authentication is not required to exploit this vulnerability. The flaw exists within the webagent.exe component which is handed requests by an Apache instance that listens by default on TCP port 443. When handling an st_upload request the process does not properly validate POST parameters used for a file creation. The contents of this newly created file are controllable via another POST variable. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: http://www.cisco.com/warp/public/707/cisco-sa-20110216-csa.shtml

## Disclosure Timeline

- 2010-09-23 - Vulnerability reported to vendor
- 2011-02-16 - Coordinated public release of advisory
