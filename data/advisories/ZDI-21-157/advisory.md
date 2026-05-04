# ZDI-21-157: (0Day) Squid Cache WCCP Protocol Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-157
- **ZDI-CAN:** ZDI-CAN-11610
- **Date:** 2021-02-09
- **CVE:** N/A
- **CVSS:** 3.7
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Squid
- **Affected Products:** Cache
- **Credit:** Lyu
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-157/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Squid Cache. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the WCCP protocol. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the "nobody" user.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 08/17/20 – ZDI reported the vulnerability to the vendor 08/17/20 – The vendor acknowledged the report 12/14/20 – ZDI requested an update 12/18/20 – ZDI requested an update 12/18/20 – The vendor indicated they were working on a fix 02/02/21 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory on 02/09/21 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2020-08-17 - Vulnerability reported to vendor
- 2021-02-09 - Coordinated public release of advisory
