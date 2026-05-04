# ZDI-23-1049: (0Day) Inductive Automation Ignition downloadLaunchClientJar Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1049
- **ZDI-CAN:** ZDI-CAN-19915
- **Date:** 2023-08-08
- **CVE:** CVE-2023-39474
- **CVSS:** 8.0
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Inductive Automation
- **Affected Products:** Ignition
- **Credit:** Nguyễn Tiến Giang (Jang) of STAR Labs SG Pte. Ltd.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1049/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Inductive Automation Ignition. User interaction is required to exploit this vulnerability in that the target must connect to a malicious server. The specific flaw exists within the downloadLaunchClientJar function. The issue results from the lack of validating a remote JAR file prior to loading it. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

01/20/23 – ZDI reported the vulnerability to the vendor. 01/23/23 – The vendor acknowledged the report. 07/18/23 – The ZDI asked for an update. 07/21/23 – The vendor states that the case is still in active development. 08/01/23 – ZDI informed the vendor that the case will be published as a zero-day advisory on 08/08/23. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-01-20 - Vulnerability reported to vendor
- 2023-08-08 - Coordinated public release of advisory
- 2023-08-08 - Advisory Updated
