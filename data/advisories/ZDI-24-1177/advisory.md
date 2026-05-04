# ZDI-24-1177: Amazon AWS CloudFormation Templates Uncontrolled Search Path Element Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1177
- **ZDI-CAN:** ZDI-CAN-24023
- **Date:** 2024-08-23
- **CVE:** N/A
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Amazon
- **Affected Products:** AWS
- **Credit:** Nitesh Surana (@_niteshsurana) of Trend Micro Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1177/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Amazon AWS. Authentication is not required to exploit this vulnerability. The specific flaw exists within the installation of AWS Simple Storage Service. When installed from the official GitHub repository, the installation attempts to load a non-existent cloud resource that is vulnerable to takeover. An attacker can leverage this vulnerability to execute code on systems dependent on the cloud resource.

## Additional Details

Amazon has issued an update to correct this vulnerability. More details can be found at: https://github.com/aws-samples/amazon-es-service-recommended-alarms/commit/6115796183fc8cf4ef505f2efe9135b4566e1f9b

## Disclosure Timeline

- 2024-04-25 - Vulnerability reported to vendor
- 2024-08-23 - Coordinated public release of advisory
- 2024-08-23 - Advisory Updated
