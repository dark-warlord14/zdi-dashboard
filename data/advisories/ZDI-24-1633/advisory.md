# ZDI-24-1633: Hewlett Packard Enterprise AutoPass License Server SQL Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1633
- **ZDI-CAN:** ZDI-CAN-24693
- **Date:** 2024-12-02
- **CVE:** CVE-2024-51769
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** AutoPass License Server
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1633/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Hewlett Packard Enterprise AutoPass License Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the web service, which listens on TCP port 5814 by default. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbgn04760en_us&docLocale=en_US

## Disclosure Timeline

- 2024-07-24 - Vulnerability reported to vendor
- 2024-12-02 - Coordinated public release of advisory
- 2024-12-02 - Advisory Updated
