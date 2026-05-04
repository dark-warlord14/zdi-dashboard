# ZDI-24-1063: Microsoft Reactor Workshops reactorworkshops Uncontrolled Search Path Element Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1063
- **ZDI-CAN:** ZDI-CAN-23028
- **Date:** 2024-08-05
- **CVE:** N/A
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Reactor Workshops
- **Credit:** Nitesh Surana (@_niteshsurana) of Trend Micro Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1063/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Reactor Workshops. Authentication is not required to exploit this vulnerability. The specific flaw exists within the installation of Reactor Workshops. When installed from the official Microsoft GitHub repository, the installation attempts to load a non-existent cloud resource that is vulnerable to takeover. An attacker can leverage this vulnerability to execute code on systems dependent on the cloud resource.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-us/security-guidance/researcher-acknowledgments-online-services

## Disclosure Timeline

- 2024-01-10 - Vulnerability reported to vendor
- 2024-08-05 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
