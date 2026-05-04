# ZDI-23-880: Microsoft Azure Machine Learning Service DSIMountAgent Missing Authentication Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-880
- **ZDI-CAN:** ZDI-CAN-19402
- **Date:** 2023-06-16
- **CVE:** CVE-2023-28312
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Azure
- **Credit:** Nitesh Surana (@_niteshsurana) of Project Nebula, Trend Micro Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-880/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on Microsoft Azure. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the DSIMountAgent service, which listens on TCP port 46802 by default. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to disclose sensitive information, leading to further compromise.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-28312

## Disclosure Timeline

- 2022-12-16 - Vulnerability reported to vendor
- 2023-06-16 - Coordinated public release of advisory
