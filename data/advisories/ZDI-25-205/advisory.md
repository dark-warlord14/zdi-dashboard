# ZDI-25-205: Amazon AWS CloudFormation Templates Uncontrolled Search Path Element Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-205
- **ZDI-CAN:** ZDI-CAN-25426
- **Date:** 2025-04-07
- **CVE:** N/A
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Amazon
- **Affected Products:** AWS
- **Credit:** Nitesh Surana (@_niteshsurana) of Trend Micro Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-205/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Amazon AWS. Authentication is not required to exploit this vulnerability. The specific flaw exists within the installation of AWS Simple Storage Service. When installed from the official GitHub repository, the installation attempts to load a non-existent cloud resource that is vulnerable to takeover. An attacker can leverage this vulnerability to execute code on systems dependent on the cloud resource.

## Additional Details

Amazon has issued an update to correct this vulnerability. More details can be found at: https://github.com/aws-samples/ecs-service-connect-yelb-sample-app/commit/2f8bd3934533a5e0b8b34c9fad1304bbe89697e8

## Disclosure Timeline

- 2024-10-03 - Vulnerability reported to vendor
- 2025-04-07 - Coordinated public release of advisory
- 2025-04-07 - Advisory Updated
