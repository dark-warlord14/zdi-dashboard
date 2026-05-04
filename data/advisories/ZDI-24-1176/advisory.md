# ZDI-24-1176: Amazon AWS aws-glue-with-s2s-vpn Uncontrolled Search Path Element Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1176
- **ZDI-CAN:** ZDI-CAN-23901
- **Date:** 2024-08-23
- **CVE:** N/A
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Amazon
- **Affected Products:** AWS
- **Credit:** Nitesh Surana (@_niteshsurana) of Trend Micro Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1176/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Amazon AWS. Authentication is not required to exploit this vulnerability. The specific flaw exists within the installation of AWS Glue. When installed from the official GitHub repository, the installation attempts to load a non-existent cloud resource that is vulnerable to takeover. An attacker can leverage this vulnerability to execute code on systems dependent on the cloud resource.

## Additional Details

Amazon has issued an update to correct this vulnerability. More details can be found at: https://github.com/aws-samples/aws-glue-with-s2s-vpn/commit/a4c587ca6110967a5a61f3a24e53a4f2910592ff

## Disclosure Timeline

- 2024-04-02 - Vulnerability reported to vendor
- 2024-08-23 - Coordinated public release of advisory
- 2024-08-23 - Advisory Updated
