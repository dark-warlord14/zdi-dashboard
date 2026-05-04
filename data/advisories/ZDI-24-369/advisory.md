# ZDI-24-369: Google cAdvisor REST API Improper Access Control Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-369
- **ZDI-CAN:** ZDI-CAN-22648
- **Date:** 2024-04-22
- **CVE:** N/A
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Google
- **Affected Products:** cAdvisor
- **Credit:** Nitesh Surana (@_niteshsurana) of Trend Micro Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-369/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Google cAdvisor. Authentication is not required to exploit this vulnerability. The specific flaw exists within the REST API endpoint, which listens on TCP port 8080 by default. The issue results from improper access control. An attacker can leverage this vulnerability to disclose information about the currently running container instance.

## Additional Details

Google has issued an update to correct this vulnerability. More details can be found at: https://github.com/google/cadvisor/pull/3463/files

## Disclosure Timeline

- 2023-11-27 - Vulnerability reported to vendor
- 2024-04-22 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
