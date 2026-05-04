# ZDI-14-051: Hewlett-Packard LeftHand Virtual SAN Appliance dbd_manager libens Unmarshalling Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-051
- **ZDI-CAN:** ZDI-CAN-1509
- **Date:** 2014-04-03
- **CVE:** CVE-2013-4841
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** LeftHand Virtual SAN
- **Credit:** e6af8de8b1d4b2b6d5ba2610cbf9cd38
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-051/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP LeftHand Virtual SAN Appliance. Authentication is not required to exploit this vulnerability. The flaw exists within the dbd_manager component which receives messages via the hydra process. This process listens on TCP port 13841. The dbd_manager uses the libens library for unmarshalling received messages, among other things. During the unmarshalling process an undersized allocation occurs followed by a copy of data to this region. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the root user.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03995204

## Disclosure Timeline

- 2012-05-13 - Vulnerability reported to vendor
- 2014-04-03 - Coordinated public release of advisory
