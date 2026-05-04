# ZDI-23-1031: (Pwn2Own) Triangle MicroWorks SCADA Data Gateway Trusted Certification Unrestricted Upload of File Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1031
- **ZDI-CAN:** ZDI-CAN-20537
- **Date:** 2023-08-04
- **CVE:** CVE-2023-39463
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Triangle MicroWorks
- **Affected Products:** SCADA Data Gateway
- **Credit:** Team ECQ
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1031/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Triangle MicroWorks SCADA Data Gateway. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the trusted certification feature. The issue lies in the handling of the OpcUaSecurityCertificateAuthorityTrustDir variable, which allows an arbitrary file write with attacker-controlled data. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Triangle MicroWorks has issued an update to correct this vulnerability. More details can be found at: https://www.trianglemicroworks.com/products/scada-data-gateway/what's-new

## Disclosure Timeline

- 2023-02-24 - Vulnerability reported to vendor
- 2023-08-04 - Coordinated public release of advisory
