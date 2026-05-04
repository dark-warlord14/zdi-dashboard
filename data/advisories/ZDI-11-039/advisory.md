# ZDI-11-039: BMC Perform Agent Service Daemon BGS_MULTIPLE_READS Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-039
- **ZDI-CAN:** ZDI-CAN-613
- **Date:** 2011-02-03
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** BMC Software
- **Affected Products:** Performance Assurance
- **Credit:** Manuel Santamarina-Suarez
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-039/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of BMC Perform Agent. Authentication is not required to exploit this vulnerability. The specific flaw exists within the service daemon which listens by default on TCP port 6768. When processing the BGS_MULTIPLE_READS commands a user-supplied length value is trusted and utilized in reading arbitrary data into a stack buffer. By providing large enough values a remote attacker can abuse this to execute remote code under the context of the SYSTEM user.

## Additional Details

BMC Performance Assurance for Servers Versions 7.4.00, 7.4.10, 7.4.15, 7.5.00, 7.5.10 January, 2011 Tracking number QM001683974: Potential vulnerability in network-accessible binary Service Daemon and Manager Daemon BMC Software is alerting users of the following products to a potential problem: - BMC Performance Analysis for Servers, versions 7.4.00 through 7.5.10 - BMC Performance Assurance for Servers, versions 7.4.00 through 7.5.10 - BMC Performance Assurance for Virtual Servers, versions 7.4.00 through 7.5.10 - BMC Performance Analyzer for Servers, versions 7.4.00 through 7.5.10 - BMC Performance Predictor for Servers, versions 7.4.00 through 7.5.10 - BMC Capacity Management Essentials 1.2.00 (7.4.15) This technical bulletin describes a patch that prevents the problem from occurring. If you have any questions about the problem or the patch, contact BMC Software Customer Support at 800 537 1813 (United States or Canada) or call your local support center. BMC Software thanks Manuel Santamarina-Suarez, of the TippingPoint Zero Day Initiative (ZDI), for reporting this issue. Potential vulnerability in network accessible binaries Service Daemon and Manager Daemon BMC Software has identified a potential security exposure in Perform binaries Service Daemon and Manager Daemon, which listen on a network port. (The default port is 6768.) This problem affects all supported versions of these products. This is a remotely exploitable memory corruption that can result in the remote execution of arbitrary code such as the Perform Installation Owner account on UNIX, or the SYSTEM account on Windows. You can correct this issue by downloading and applying the appropriate patch for your operating system and version of these products.

## Disclosure Timeline

- 2009-10-27 - Vulnerability reported to vendor
- 2011-02-03 - Coordinated public release of advisory
