# ZDI-17-826: Dell EMC VNX Monitoring and Reporting RMI Registry Deserialization of Untrusted Data Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-826
- **ZDI-CAN:** ZDI-CAN-4807
- **Date:** 2017-09-26
- **CVE:** CVE-2017-8012
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:L/Au:S/C:N/I:N/A:C
- **Affected Vendors:** Dell EMC
- **Affected Products:** VNX Monitoring and Reporting
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-826/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial of service on vulnerable installations of Dell EMC VNX Monitoring and Reporting. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within an exposed RMI registry, which listens on TCP port 52569 by default. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to create a denial-of-service condition to users of the system.

## Additional Details

Dell EMC has issued an update to correct this vulnerability. More details can be found at: http://seclists.org/fulldisclosure/2017/Sep/51

## Disclosure Timeline

- 2017-05-09 - Vulnerability reported to vendor
- 2017-09-26 - Coordinated public release of advisory
