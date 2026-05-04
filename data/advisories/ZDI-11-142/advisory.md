# ZDI-11-142: IBM solidDB solid.exe rpc_test_svc Commands Multiple DoS Vulnerabilities

## Metadata

- **ZDI ID:** ZDI-11-142
- **ZDI-CAN:** ZDI-CAN-1000
- **Date:** 2011-04-26
- **CVE:** CVE-2011-1208
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:N/A:C
- **Affected Vendors:** IBM
- **Affected Products:** solidDB
- **Credit:** Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-142/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial of service condition on vulnerable installations of IBM SolidDB. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the rpc_test_svc_readwrite and rpc_test_svc_done commands. By issuing these commands remotely to TCP port 2315, an attacker can cause the solidDB.exe process to dereference a NULL pointer and subsequently crash.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: https://www-304.ibm.com/support/docview.wss?uid=swg21496106

## Disclosure Timeline

- 2010-11-07 - Vulnerability reported to vendor
- 2011-04-26 - Coordinated public release of advisory
