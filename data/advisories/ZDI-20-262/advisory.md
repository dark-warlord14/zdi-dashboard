# ZDI-20-262: (0Day) WECON LeviStudioU G_bmp szFilename Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-262
- **ZDI-CAN:** ZDI-CAN-9280
- **Date:** 2020-02-20
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** WECON
- **Affected Products:** LeviStudioU
- **Credit:** Natnael Samson (@NattiSamson)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-262/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Wecon LeviStudioU. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of XML files. When parsing the szFilename attribute of the G_bmp element, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of an administrator.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 09/27/19 - ZDI provided the vulnerability report to ICS-CERT 09/30/19 - ICS-CERT acknowledged the report and provided an ICS-VU# 01/24/20 - ZDI requested any available update about the report 01/24/20 - ICS-CERT indicated the vendor had acknowledged the report, but that no further update was available 02/10/20 - ZDI notified ICS-CERT of the intent to publish the report as 0-day on 02/20/20 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting.

## Disclosure Timeline

- 2019-09-27 - Vulnerability reported to vendor
- 2020-02-20 - Coordinated public release of advisory
