# ZDI-18-132: (0Day) Belkin NetCam SetSmartDevURL Server-Side Request Forgery Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-132
- **ZDI-CAN:** ZDI-CAN-4970
- **Date:** 2018-01-23
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Belkin
- **Affected Products:** NetCam
- **Credit:** Dove Chiu Kenney Lu and Tim Yeh of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-132/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Belkin NetCam. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of requests to the Wemo SetSmartDevURL API. A crafted request can trigger execution of a system call composed from a user-supplied string. An attacker can leverage this vulnerability to execute code under the context of root.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 07/11/17 - ZDI reported vulnerability to vendor 07/11/17 - Vendor acknowledged 11/22/17 - ZDI contacted vendor requesting an status update 01/18/18 - ZDI notified the vendor the intention to 0-day the case -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting.

## Disclosure Timeline

- 2017-07-11 - Vulnerability reported to vendor
- 2018-01-23 - Coordinated public release of advisory
