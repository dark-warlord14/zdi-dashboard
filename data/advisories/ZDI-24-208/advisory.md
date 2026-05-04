# ZDI-24-208: Microsoft Azure MCR VSTS CLI vstscli Uncontrolled Search Path Element Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-208
- **ZDI-CAN:** ZDI-CAN-23012
- **Date:** 2024-02-26
- **CVE:** N/A
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Azure
- **Credit:** Nitesh Surana (@_niteshsurana) of Trend Micro Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-208/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of MCR VSTS CLI for Microsoft Azure. Authentication is not required to exploit this vulnerability. The specific flaw exists within the installation of MCR VSTS CLI. When installed from the Microsoft Container Registry, the installation attempts to load a non-existent cloud resource that is vulnerable to takeover. An attacker can leverage this vulnerability to execute code on systems dependent on the cloud resource.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-us/security-guidance/researcher-acknowledgments-online-services

## Disclosure Timeline

- 2024-01-10 - Vulnerability reported to vendor
- 2024-02-26 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
