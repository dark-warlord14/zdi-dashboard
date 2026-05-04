# ZDI-22-387: (0Day) Fuji Electric Alpha5 C5V File Parsing Uninitialized Pointer Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-387
- **ZDI-CAN:** ZDI-CAN-13876
- **Date:** 2022-02-22
- **CVE:** CVE-2022-21168
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Fuji Electric
- **Affected Products:** Alpha5
- **Credit:** xina1i
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-387/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Fuji Electric Alpha5. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of C5V files. The issue results from the lack of proper initialization of a pointer prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 06/04/2021 – ZDI reported the vulnerability to ICS-CERT 10/05/2021 – ZDI requested the advisory link 10/18/2021 – ZDI requested an update 10/18/2021 – ICS-CERT indicated that the cases have been fixed 11/19/2021 – ZDI requested an update 01/11/2022 – ZDI requested the advisory link 02/14/2022 – ZDI notified ICS-CERT of the intention to publish the cases as 0-day advisories on 02/21/22

## Disclosure Timeline

- 2021-06-04 - Vulnerability reported to vendor
- 2022-02-22 - Coordinated public release of advisory
- 2022-03-23 - Advisory Updated
