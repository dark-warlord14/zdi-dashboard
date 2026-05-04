# ZDI-17-505: Dell EMC VNX Monitoring and Reporting Scheduler Static Credentials Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-505
- **ZDI-CAN:** ZDI-CAN-4768
- **Date:** 2017-08-01
- **CVE:** CVE-2017-8011
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Dell EMC
- **Affected Products:** VNX Monitoring and Reporting
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-505/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Dell EMC VNX Monitoring and Reporting. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the Scheduler class. An attacker can use the static credentials to access VNX Webservice Gateway service's API to execute arbitrary code under the context of SYSTEM.

## Additional Details

Dell EMC has issued an update to correct this vulnerability. More details can be found at: http://seclists.org/fulldisclosure/2017/Jul/21

## Disclosure Timeline

- 2017-05-04 - Vulnerability reported to vendor
- 2017-08-01 - Coordinated public release of advisory
