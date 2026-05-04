# ZDI-12-166: (0Day) HP LeftHand Virtual SAN Appliance Unauthenticated Access Remote Command Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-166
- **ZDI-CAN:** ZDI-CAN-1467
- **Date:** 2012-08-22
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** LeftHand Virtual SAN
- **Credit:** e6af8de8b1d4b2b6d5ba2610cbf9cd38
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-166/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP LeftHand Virtual SAN Appliance. Authentication is not required to exploit this vulnerability. The flaw exists within the hydra component which listens by default on 13841/tcp. The hydra daemon is responsible for management remote operations such as user creation, snapshots, etc. Insufficient authentication is performed prior to performing administrative level tasks. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 180 day deadline.

## Disclosure Timeline

- 2011-12-22 - Vulnerability reported to vendor
- 2012-08-22 - Coordinated public release of advisory
