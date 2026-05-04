# ZDI-25-609: Cisco Identity Services Engine invokeStrongSwanShellScript Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-609
- **ZDI-CAN:** ZDI-CAN-27121
- **Date:** 2025-07-17
- **CVE:** CVE-2025-20281
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Cisco
- **Affected Products:** Identity Services Engine
- **Credit:** Bobby Gould (@bobbygould5) of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-609/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Cisco Identity Services Engine. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the invokeStrongSwanShellScript method. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-unauth-rce-ZAd2GnJ6

## Disclosure Timeline

- 2025-05-02 - Vulnerability reported to vendor
- 2025-07-17 - Coordinated public release of advisory
- 2025-07-17 - Advisory Updated
