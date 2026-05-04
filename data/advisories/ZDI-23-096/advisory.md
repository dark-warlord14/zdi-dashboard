# ZDI-23-096: Microsoft Azure Machine Learning Service Cleartext Storage of Credentials Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-096
- **ZDI-CAN:** ZDI-CAN-19057
- **Date:** 2023-02-07
- **CVE:** N/A
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Azure
- **Credit:** Nitesh Surana (@_niteshsurana) of Project Nebula, Trend Micro Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-096/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on Microsoft Azure. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of credentials within Azure Machine Learning Service workbooks. The issue results from storing sensitive information in plaintext. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Fixed in an online service update on October 31, 2022

## Disclosure Timeline

- 2022-10-04 - Vulnerability reported to vendor
- 2023-02-07 - Coordinated public release of advisory
