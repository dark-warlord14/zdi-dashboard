# ZDI-24-1719: (0Day) Arista NG Firewall ReportEntry SQL Injection Arbitrary File Read and Write Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1719
- **ZDI-CAN:** ZDI-CAN-24325
- **Date:** 2024-12-19
- **CVE:** CVE-2024-12832
- **CVSS:** 8.3
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:L
- **Affected Vendors:** Arista
- **Affected Products:** NG Firewall
- **Credit:** Mehmet INCE (@mdisec) from PRODAFT.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1719/
## Vulnerability Details

This vulnerability allows remote attackers to create arbitrary files and disclose sensitive information on affected installations of Arista NG Firewall. Authentication is required to exploit this vulnerability. The specific flaw exists within the ReportEntry class. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the www-data user.

## Additional Details

07/03/24 – ZDI reported the vulnerability to the vendor 08/07/24 – the vendor acknowledged the receipt of the report 11/18/24 - ZDI asked for updates 11/21/24 - ZDI asked for updates 12/10/24 - ZDI notified the vendor of the intention to publish the cases as a 0-day advisory Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application

## Disclosure Timeline

- 2024-07-03 - Vulnerability reported to vendor
- 2024-12-19 - Coordinated public release of advisory
- 2024-12-19 - Advisory Updated
