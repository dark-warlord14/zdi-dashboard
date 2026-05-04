# ZDI-25-248: (0Day) eCharge Hardy Barth cPH2 nwcheckexec.php dest Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-248
- **ZDI-CAN:** ZDI-CAN-23114
- **Date:** 2025-04-23
- **CVE:** CVE-2025-3882
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** eCharge Hardy Barth
- **Affected Products:** cPH2
- **Credit:** adhkr - LuwakLab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-248/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of eCharge Hardy Barth cPH2 charging stations. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the dest parameter provided to the nwcheckexec.php endpoint. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the www-data user.

## Additional Details

03/14/24 – ZDI contacted the vendor via email to info@echarge.de 10/28/24 – ZDI reached out to echarge’s support team 04/12/25 – ZDI informed the vendor that since we have not received a response, we will publish the report as a zero-day advisory

## Disclosure Timeline

- 2025-03-11 - Vulnerability reported to vendor
- 2025-04-23 - Coordinated public release of advisory
- 2025-04-23 - Advisory Updated
