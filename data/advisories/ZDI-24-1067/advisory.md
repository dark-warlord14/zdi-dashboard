# ZDI-24-1067: Microsoft Azure CollectSFData docs-analytics-eus Uncontrolled Search Path Element Impersonation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1067
- **ZDI-CAN:** ZDI-CAN-23055
- **Date:** 2024-08-05
- **CVE:** N/A
- **CVSS:** 9.4
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:L
- **Affected Vendors:** Microsoft
- **Affected Products:** Azure
- **Credit:** Nitesh Surana (@_niteshsurana) of Trend Micro Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1067/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of CollectSFData for Microsoft Azure. Authentication is not required to exploit this vulnerability. The issue results from a reference to a non-existent cloud resource that is vulnerable to takeover. An attacker can leverage this vulnerability to execute code on systems dependent on the cloud resource.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-us/security-guidance/researcher-acknowledgments-online-services

## Disclosure Timeline

- 2024-01-10 - Vulnerability reported to vendor
- 2024-08-05 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
