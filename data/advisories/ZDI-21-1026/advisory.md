# ZDI-21-1026: (0Day) D-Link DIR-2055 HNAP PrivateLogin Incorrect Implementation of Authentication Algorithm Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1026
- **ZDI-CAN:** ZDI-CAN-12686
- **Date:** 2021-08-26
- **CVE:** N/A
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DIR-2055
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1026/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of D-Link DIR-2055 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of HNAP login requests. The issue results from the lack of proper implementation of the authentication algorithm. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the router.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 03/31/21 – ZDI reported the vulnerabilities to the vendor/ICS-CERT 08/04/21 – ZDI requested an update 08/09/21 – The vendor indicated they would provide more details the following day 08/17/21 – The vendor indicated they were still waiting for updated details 08/18/20 – ZDI notified the vendor of the intention to publish the cases as 0-day advisories on 08/26/21 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2021-03-31 - Vulnerability reported to vendor
- 2021-08-26 - Coordinated public release of advisory
