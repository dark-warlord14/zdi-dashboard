# ZDI-24-1068: Microsoft Azure ML.NET Samples mlnetfilestorage Uncontrolled Search Path Element Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1068
- **ZDI-CAN:** ZDI-CAN-23066
- **Date:** 2024-08-05
- **CVE:** N/A
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Azure
- **Credit:** Nitesh Surana (@_niteshsurana) of Trend Micro Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1068/
## Vulnerability Details

This vulnerability allows remote attackers to manipulate sample datasets on affected installations of ML.NET Samples for Microsoft Azure. Authentication is not required to exploit this vulnerability. The specific flaw exists within the installation of ML.NET Samples. When installed from the official Microsoft GitHub repository, the installation attempts to load a non-existent cloud resource that is vulnerable to takeover. An attacker can leverage this vulnerability to manipulate sample datasets on systems dependent on the cloud resource.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-us/security-guidance/researcher-acknowledgments-online-services

## Disclosure Timeline

- 2024-01-12 - Vulnerability reported to vendor
- 2024-08-05 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
