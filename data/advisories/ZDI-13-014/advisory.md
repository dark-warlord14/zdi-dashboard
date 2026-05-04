# ZDI-13-014: Hewlett-Packard LeftHand Virtual SAN Appliance Hydra Ping Hostname Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-014
- **ZDI-CAN:** ZDI-CAN-1513
- **Date:** 2013-02-11
- **CVE:** CVE-2012-3285
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** LeftHand Virtual SAN
- **Credit:** e6af8de8b1d4b2b6d5ba2610cbf9cd38
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-014/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP LeftHand Virtual SAN Appliance. Authentication is not required to exploit this vulnerability. The flaw exists within the hydra service, specifically with the LHNModParam component. This process listens on TCP port 13838. When attempting to service an application level ping request, the process fails to properly verify the length of the hostname parameter before copying to a local stack buffer. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the root user.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay?docId=emr_na-c03661318

## Disclosure Timeline

- 2012-03-14 - Vulnerability reported to vendor
- 2013-02-11 - Coordinated public release of advisory
